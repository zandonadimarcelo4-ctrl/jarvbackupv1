from pathlib import Path
text = Path('agents/OpenDevin/openhands/runtime/impl/fusion/fusion_runtime.py').read_text()
start = text.find('        lines = "Perfis ativos:"')
end = text.find('    def _build_planner')
print(text[start:end])
