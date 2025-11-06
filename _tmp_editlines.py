from pathlib import Path
path = Path('agents/OpenDevin/openhands/runtime/impl/fusion/fusion_runtime.py')
lines = path.read_text().splitlines()
for idx, line in enumerate(lines):
    if line.strip() == 'snippet = tpl.system_prompt.strip().replace("':
        lines[idx] = '        for tpl in templates:'  # placeholder? Wait this would remove line. Need to restructure
