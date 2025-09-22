from . import web, system

actions = {
    "open_browser" : web.open_browser,
    "read_first_paragraph" : web.open_browser,
    "send_email" : system.send_email
}

def execute_command(intent):
    action = intent.action
    parameters = intent.parameters if intent.parameters else {}

    if action not in actions:
        raise ValueError(f"Unknown action: {action}")
    
    filled_parameters = {p[0] : p[1] for p in parameters if p[1]}
    return actions[action](**filled_parameters)