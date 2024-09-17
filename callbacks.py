from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.outputs.llm_result import LLMResult

from typing import Any, Dict, List

class AgentCallbackHandler(BaseCallbackHandler):
  def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
    """Run when LLM starts running."""
    print(f"******LLM started running with prompt {prompts[0]}")
    print('******')

  def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
    """Run when LLM ends running."""
    print(f"******LLM ended running with response {response.generations[0][0]}")
    print('******')

