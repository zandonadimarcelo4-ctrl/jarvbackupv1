from pathlib import Path
text = Path('code_base/langgraph_manus_agent.py').read_text()
old = "        prompt = (\n            \"Você é Manus, engenheira de software. Gere um relatório final curto para o usuário.\\n\"\n            f\"Objetivo: {state['input']}\\n\"\n            f\"Histórico de passos:\\n{bullet_summary}\\n\"\n            \"Explique o que foi feito e destaque próximos passos se necessário.\"\n        )\n        final_response = self._planner_llm.invoke(prompt)\n"
new = "        prompt = (\n            \"Você é Manus, engenheira de software. Gere um relatório final curto para o usuário.\\n\"\n            f\"Objetivo: {state['input']}\\n\"\n            f\"Histórico de passos:\\n{bullet_summary}\\n\"\n            \"Explique o que foi feito e destaque próximos passos se necessário.\"\n        )\n        memory_context = self._vector_context(state['input'])\n        if memory_context:\n            prompt += f\"\\nMemoria relevante:\\n{memory_context}\\n\"\n        if self._role_context:\n            prompt += f\"\\nPerfis de atuacao:\\n{self._role_context}\\n\"\n        final_response = self._planner_llm.invoke(prompt)\n"
if old not in text:
    raise SystemExit('synthesizer block not found')
text = text.replace(old, new, 1)
Path('code_base/langgraph_manus_agent.py').write_text(text)
