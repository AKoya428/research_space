from ast import Param
from dataclasses import dataclass
from external_api import const
from external_api.logger import BaseLogger
from openai import AsyncOpenAI
import asyncio
import os


@dataclass
class GPTResponse:
    """ChatGPTの返り値を定義するクラス"""

    content: str
    finish_reason: str = ""
    error: str = ""


async def post_chatgpt(
    client,
    prompt: str,
    semaphore,
    *,
    max_token: int = None,
) -> GPTResponse:
    async with semaphore:
        try:
            res = await client.chat.completions.create(
                model="gpt-5",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_completion_tokens=max_token if max_token else const.MAX_TOKEN,
            )
            # レスポンスのテキストを取得
            content = res.choices[0].message.content.strip()
            finish_reason = res.choices[0].finish_reason
            return GPTResponse(
                content=content,
                finish_reason=finish_reason,
            )

        except Exception as e:
            return GPTResponse(
                content="",
                finish_reason="",
                error=f"{e}",
            )


class GPTHandler:
    """chatGPTのハンドラー"""

    @classmethod
    def generate_client(cls):
        """API clientを作成する"""
        client = AsyncOpenAI(api_key=os.getenv("GPT_API_KEY"))
        return client

    @classmethod
    def post_list(
        cls,
        prompts: list,
        *,
        max_token: int = None,
    ) -> list[GPTResponse]:
        """chatGPTにリクエストを送信する"""
        semaphore = asyncio.Semaphore(const.SEMAPHORE)
        client = cls.generate_client()

        async def run_all():
            try:
                tasks = [
                    post_chatgpt(client, p, semaphore, max_token=max_token)
                    for p in prompts
                ]
                return await asyncio.gather(*tasks)
            finally:
                await client.close()

        return asyncio.run(run_all())
