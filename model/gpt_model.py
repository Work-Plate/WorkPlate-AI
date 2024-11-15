from openai import OpenAI

class GPTModel:
    def __init__(self):
        self.client = OpenAI()

    def generate_response(self, prompt: str, user_message: str) -> str:
        """
        프롬프트와 사용자 메시지가 주어지면 GPT의 결과를 반환합니다.
        :param prompt: 사용하려는 프롬프트
        :param user_message: 사용자 메시지
        :return: 생성된 결과 메시지
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content