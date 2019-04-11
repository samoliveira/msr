from git import Repo
import os, os.path
import platform
import time
import datetime
from datetime import date, timedelta


class edge:
	def __init__(self, file1, file2):
		self.file1 = file1
		self.file2 = file2
		self.weight = 1



graph = {}

dir = 'C:\\Users\\samue\\EventBus'

repo = Repo(dir)
all_commits = list(repo.iter_commits('master'))

def create_edge(all_commits):
	for commit in all_commits:
		commit_files = commit.stats.files.keys()
		
		for i in range(len(commit_files)):
			if commit_files[i].endswith(".java"):
				if commit_files[i] not in graph:
					graph[commit_files[i]] = {}
				for j in range(i+1, len(commit_files)):
					if commit_files[j].endswith(".java"):
						if commit_files[j] not in graph:
							graph[commit_files[j]] = {}
						if commit_files[i] not in graph[commit_files[j]]:
							graph[commit_files[j]][commit_files[i]] = 0
							
						if commit_files[j] not in graph[commit_files[i]]:
							graph[commit_files[i]][commit_files[j]] = 0
						
						graph[commit_files[i]][commit_files[j]] += 1
						graph[commit_files[j]][commit_files[i]] += 1
						#print graph[commit_files[i]]		
		
create_edge(all_commits)

def max_weight(G):
	max = 0
	files = {"file1": "", "file2": ""}
	for file1, dc in G.items():
		for file2, weight in dc.items():
			if max < weight:
				max = weight
				files["file1"] = file1
				files["file2"] = file2
	print files, max

def max_rel(G):
	max = 0
	file = ""
	for file_name, dc in G.items():
		number_file = len(dc.keys())
		if max < number_file:
			max = number_file
			file = file_name	
	print file, max
def max_sum_weight(G):
	max = 0
	file = ""
	for file1, dc in G.items():
		sum = 0
		for file2, weight in dc.items():
			sum += weight
		if max < sum:
			max = sum
			file = file1
	print file, max


print "Questao 1"
max_weight(G=graph)
print "Questao 2"
max_rel(G=graph)
print "Questao 3"
max_sum_weight(G=graph)

 