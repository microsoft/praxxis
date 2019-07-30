
def add_output(args, output_root, current_scene_db):
    import json
    from src.praxxis.sqlite import sqlite_scene
    from src.praxxis.display import display_notebook

    CELL_FORMAT = {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [{"name": "stdout", "output_type": "stream", "text": []}],  'source': ['OUTPUT ADDED AFTER EXECUTION:']}
    
    CELL_FORMAT['outputs'][0]['text'].append(args.string)

    last_notebook = sqlite_scene.get_recent_history(current_scene_db, 1)
    if last_notebook == []:
        from src.praxxis.util.error import EmptyRulesetError
        raise EmptyRulesetError()
       
    with open(last_notebook[0][1]) as f:
        notebook_data = json.load(f)
        notebook_data["cells"].append(CELL_FORMAT)
        f.close()
    with open(last_notebook[0][1], 'w') as f1:
        json.dump(notebook_data, f1)
        f1.close()
        
    display_notebook.display_adding_output(last_notebook[0][0], args.string)
    
