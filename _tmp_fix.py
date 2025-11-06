from pathlib import Path
path = Path('agents/OpenDevin/openhands/runtime/impl/fusion/fusion_runtime.py')
text = path.read_text()
text = text.replace('snippet = tpl.system_prompt.strip().replace("\n", " \n', 'snippet = tpl.system_prompt.strip().replace("\\n", " ")\n', 1)
