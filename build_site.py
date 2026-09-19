import json
from pathlib import Path 
from datetime import date 

def upcoming(events, today):
    future = [e for e in events if e["date"] >= today]
    return sorted(future, key=lambda e: e["date"]) 


def load_events(path): 
    data = json.loads(Path(path).read_text())
    return data["events"]

def render(events): 
    items = "\n".join(f' <li><strong>{e["date"]}</strong> - {e["title"]}'
    f' <em>({e["venue"]})</em></li>'
    for e in events
    )
    return (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        ' <meta charset="utf-8">\n'
        ' <title>ACM Club at CST - Events</title>\n'
        '</head>\n'
        '<body>\n'
        ' <h1>Upcoming events</h1>\n'
        ' <ul>\n'
        f'{items}\n'
        ' </ul>\n'
        '</body>\n'
        '</html>\n')


def main():
    events = upcoming(load_events("events.json"), date.today().isoformat())
    Path("dist").mkdir(exist_ok=True)
    Path("dist/index.html").write_text(render(events))
    print(f"wrote dist/index.html with {len(events)} events")

    
if __name__ == "__main__":
    main()