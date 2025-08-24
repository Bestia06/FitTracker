import os
from typing import Dict, List, Optional

import requests


class APINinjaService:
    """Service for interacting with API Ninja"""

    def __init__(self):
        self.api_key = os.getenv("API_NINJA_KEY")
        self.base_url = os.getenv("API_NINJA_BASE_URL", "https://api.api-ninjas.com/v1")

    def _make_request(self, endpoint: str, params: Dict = None) -> Optional[Dict]:
        """Make a request to API Ninja"""
        if not self.api_key:
            raise ValueError("API_NINJA_KEY environment variable is not set")

        url = f"{self.base_url}/{endpoint}"
        headers = {"X-Api-Key": self.api_key}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error making request to API Ninja: {e}")
            return None

    def get_nutrition_info(self, query: str) -> Optional[List[Dict]]:
        """Get nutrition information for a food item"""
        params = {"query": query}
        return self._make_request("nutrition", params)

    def get_exercise_info(self, name: str) -> Optional[List[Dict]]:
        """Get exercise information by name"""
        params = {"name": name}
        return self._make_request("exercises", params)

    def get_exercises_by_muscle(self, muscle: str) -> Optional[List[Dict]]:
        """Get exercises by muscle group"""
        params = {"muscle": muscle}
        return self._make_request("exercises", params)

    def get_exercises_by_type(self, type: str) -> Optional[List[Dict]]:
        """Get exercises by type (strength, cardio, etc.)"""
        params = {"type": type}
        return self._make_request("exercises", params)


# Create a singleton instance
api_ninja_service = APINinjaService()
