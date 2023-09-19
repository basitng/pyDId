import time
import requests
from typing import Dict


class DIdAPIClient:
    BASE_URL = 'https://api.d-id.com'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _send_request(self, endpoint: str, data: dict = None, files=None, method='GET') -> Dict:
        url = f'{DIdAPIClient.BASE_URL}{endpoint}'
        headers = {
            'Authorization': f'Basic {self.api_key}'
        }
        response = requests.request(
            method, url, headers=headers, json=data, files=files)

        if response.status_code == 200:
            return response.json()
        else:
            print(response)
            return response.text

    def create_talk(self, source_url: str, script: dict, config: dict) -> Dict:
        endpoint = '/talks'
        data = {
            "source_url": source_url,
            "script": script,
            "config": config
        }
        return self._send_request(endpoint, data, method='POST')

    def get_actors(self) -> Dict:
        endpoint = '/clips/actors'
        return self._send_request(endpoint)

    def get_present_driver(self, actor_name: str) -> Dict:
        endpoint = f'/clips/actors/{actor_name}/drivers'
        return self._send_request(endpoint)

    def create_clip(self, source_url: str, script: dict, provider: dict, presenter_id: str, driver_id: str, background: dict) -> Dict:
        endpoint = '/clips'
        data = {
            "source_url": source_url,
            "script": script,
            "provider": provider,
            "presenter_id": presenter_id,
            "driver_id": driver_id,
            "background": background
        }
        return self._send_request(endpoint, data, method='POST')

    def create_animation(self, source_url: str, driver_url: str, config: dict) -> Dict:
        endpoint = '/animations'
        data = {
            "source_url": source_url,
            "driver_url": driver_url,
            "config": config
        }
        return self._send_request(endpoint, data, method='POST')

    def get_voices(self) -> Dict:
        endpoint = '/tts/voices'
        return self._send_request(endpoint)

    def upload_image(self, image_file) -> Dict:
        endpoint = '/images'
        files = {'image': image_file}
        return self._send_request(endpoint, files=files, method='POST')

    def delete_image(self, image_id: str) -> Dict:
        endpoint = f'/images/{image_id}'
        return self._send_request(endpoint, method='DELETE')

    def upload_audio(self, audio_file_path: str) -> Dict:
        endpoint = "/audios"
        files = {"audio": (audio_file_path, open(
            audio_file_path, "rb"), "audio/mpeg")}
        return self._send_request(endpoint, files=files, method='POST')

    def delete_audio(self, audio_id: str) -> Dict:
        endpoint = f'/audios/{audio_id}'
        return self._send_request(endpoint, method='DELETE')

    def get_credits(self) -> Dict:
        endpoint = "/credits"
        return self._send_request(endpoint, method='GET')

    def upload_logo(self, logo_file_path: str) -> Dict:
        endpoint = "/settings/logo"
        file_extension = logo_file_path.split(".")[-1]
        content_type = f"image/{file_extension}"

        files = {"logo": (logo_file_path, open(
            logo_file_path, "rb"), content_type)}

        return self._send_request(endpoint, files=files, method='POST')

    def delete_logo(self) -> Dict:
        endpoint = "/settings/logo"
        return self._send_request(endpoint, method='DELETE')

    def get_results(self, result_id: str, target: str) -> Dict:
        while True:
            if target not in ['animations', 'clips', 'talks']:
                raise ValueError("Unsupported target")

            if target == 'animations':
                endpoint = f'/animations/{result_id}'
            elif target == 'clips':
                endpoint = f'/clips/{result_id}'
            elif target == 'talks':
                endpoint = f'/talks/{result_id}'

            response = self._send_request(endpoint)

            if response and isinstance(response, dict):
                task_status = response.get('status')

                if task_status == 'done':
                    return response  # Return the final response when the task is done
                elif task_status == 'created':
                    print("Task is pending. Waiting for it to start...")
                else:
                    print(f"Task is {task_status}.")
            else:
                print("Waiting for task to start...")

            time.sleep(2)
