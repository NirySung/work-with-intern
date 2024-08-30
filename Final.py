# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:26:07 2024

@author: A127895
"""

import numpy as np
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Specify the directory path
root_dir = r'C:\Users\A127895\Desktop\8. Python\2024.07.29 - TSM data collector\raw data\LEG1\125C24H_24020133LEG1'
# Specify the letter to search for in folder names
target_letter = 'A'


def process_files():
    all_results = []
    folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f)) and target_letter in f]
    for folder in folders:
        folder_path = os.path.join(root_dir, folder)
        dat_files = [f for f in os.listdir(folder_path) if f.endswith('.dat')]
        
        for file in dat_files:
            file_path = os.path.join(folder_path, file)
            warpagedata = np.loadtxt(file_path)
            data = warpagedata.flatten().tolist()
            
            max_element = np.max(data)
            min_element = np.min(data)
            median_element = np.median(data)
            std_dev_element = np.std(data)
            avg_element = np.average(data)
            
            all_results.append({
                'folder': folder,
                'file': file,
                'max': max_element,
                'min': min_element,
                'median': median_element,
                'std_dev': std_dev_element,
                'avg': avg_element,
                'data': data
            })
    
    return all_results

# Function to search for results
def search_results():
    search_term = entry.get().lower()
    results = process_files()
    
    found_results = [result for result in results if search_term in result['file'].lower()]
    
    if found_results:
        result_text = ""
        for result in found_results:
            result_text += f"Folder: {result['folder']}\n"
            result_text += f"File: {result['file']}\n"
            result_text += f"Maximum element: {result['max']}\n"
            result_text += f"Minimum element: {result['min']}\n"
            result_text += f"Median element: {result['median']}\n"
            result_text += f"Standard deviation: {result['std_dev']}\n"
            result_text += f"Average element: {result['avg']}\n\n"
        
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_text_widget = tk.Text(result_window, wrap=tk.WORD)
        result_text_widget.insert(tk.END, result_text)
        result_text_widget.pack(expand=True, fill=tk.BOTH)
        
        # box plot
        data_to_plot = [result['data'] for result in found_results]
        plt.figure(figsize=(10, 6))
        plt.boxplot(data_to_plot)
        plt.title('Box Plot of Warpage Data')
        plt.ylabel('Values')
        plt.xticks([])
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.show()
    else:
        messagebox.showinfo("No Results", "No matching files found.")

# Main window
root = tk.Tk()
root.title("DAT File Search")

# input field
entry_label = tk.Label(root, text="輸入 .dat 檔案名稱 :")
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# search button
search_button = tk.Button(root, text="Search", command=search_results)
search_button.pack()

# GUI event loop
root.mainloop()
