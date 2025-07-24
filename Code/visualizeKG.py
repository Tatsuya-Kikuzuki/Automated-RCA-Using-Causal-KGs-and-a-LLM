# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:10:41 2024

@author: kikuzuki
"""
import os
import re
import graphviz
import pickle

def viz_kg(kg, kg_format = 'pdf'):
    
    cleanr = re.compile('<.*?>')
    for i in range(len(kg["nodes"])):
        kg["nodes"][i]["label"] = re.sub(cleanr, ' ', kg["nodes"][i]["label"])
    
    dot = graphviz.Digraph(format = kg_format)
    dot.attr('node', fontname = 'Meiryo UI')
    dot.attr('edge', fontname = 'Meiryo UI')

    for node in kg["nodes"]:
        dot.node(node["id"], node["label"])

    for edge in kg["edges"]:
        edge_color = "black"
        for condition in kg["conditions"]:
            if edge["id"] in condition["edges"]:
                if condition["type"] == "AND":
                    edge_color = "red"
                elif condition["type"] == "OR":
                    edge_color = "blue"
                break
                
        dot.edge(edge["source"], edge["target"], label = edge["relation"], color=edge_color)

    
    
    return dot


if __name__ == '__main__':
        
    filename_kg = "db/db_kg/kgs.bin"
    viewname_kg = "db/db_kg/db_kg_view"
    
    if not os.path.isfile(viewname_kg + ".pdf"):
        try:
            with open(filename_kg, 'rb') as p:
                kg = pickle.load(p)
            
            # visualize                
            dot = viz_kg(kg)
            dot.render('./' + viewname_kg, view=False) # : to export to the file
            
            # analyze
            nodes_dict = {}
            nodes_dup  = {}
            for node in kg["nodes"]:
                metadata = node["metadata"]
                label = node["label"]
                for meta_each in metadata:
                    if meta_each[0] not in nodes_dict:
                        nodes_dict[meta_each[0]] = []
                    nodes_dict[meta_each[0]].append(label)
                if len(metadata) > 1:
                    nodes_dup[label] = metadata
            print(viewname_kg + ".pdf successfully constructed!")
        except Exception as e:
            print(str(e))
    else:
        print(viewname_kg + ".pdf already exists.")
