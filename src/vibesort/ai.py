import os
from typing_extensions import Literal
import openai
from pydantic import BaseModel
from typing import TypeVar, Any


class VibesortResponse(BaseModel):
    sorted_array: list[int]


class VibesortRequest(BaseModel):
    array: list[int]
    order: Literal["asc", "desc"] = "asc"


class VibeequalsResponse(BaseModel):
    are_equal: bool
    reasoning: str


class VibeequalsRequest(BaseModel):
    value1: Any
    value2: Any


def vibesort(array: list[int]) -> list[int]:
    return structured_output(
        content=VibesortRequest(array=array).model_dump_json(),
        response_format=VibesortResponse,
    ).sorted_array


def vibeequals(value1: Any, value2: Any) -> bool:
    """
    Uses AI to determine if two values are semantically/vibrationally equal.
    
    Args:
        value1: First value to compare
        value2: Second value to compare
        
    Returns:
        bool: True if the values are considered equal by AI, False otherwise
    """
    prompt = f"""
    Compare these two values to determine if they are semantically or conceptually equal, 
    even if they may differ in format, representation, or exact wording.
    
    Consider things like:
    - Similar meanings expressed differently
    - Different representations of the same concept
    - Equivalent values in different formats
    - Synonymous expressions
    
    Value 1: {value1}
    Value 2: {value2}
    
    Please provide a boolean result and brief reasoning for your decision.
    """
    
    request = VibeequalsRequest(value1=value1, value2=value2)
    
    response = structured_output(
        content=prompt,
        response_format=VibeequalsResponse,
    )
    
    return response.are_equal


T = TypeVar("T", bound=BaseModel)


def structured_output(
    content: str,
    response_format: T,
    model: str = "gpt-4.1-mini",
) -> T:
    api_key = os.environ["OPENAI_API_KEY"]
    client = openai.OpenAI(api_key=api_key)

    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content,
                    },
                ],
            }
        ],
        response_format=response_format,
    )
    response_model = response.choices[0].message.parsed
    return response_model
