from git import Repo
import time 
import operator 
from difflib import unified_diff
import os, os.path
from sets import Set
import collections

dir = 'C:\\Users\\samue\\EventBus'

repo = Repo(dir)
assert not repo.bare
all_commits = list(repo.iter_commits('master'))

#repo.git.checkout(all_commits[0])
#cpt = sum([len(files) for r, d, files in os.walk(dir)])

#print(cpt)

#repo.git.checkout(all_commits[-1])
#cpt = sum([len(files) for r, d, files in os.walk(dir)])

#print(cpt)

def get_all_commits_by_year_interval(all_commits, begin, end):
	result_commits = []
	for commit in all_commits:
		commit_year = time.gmtime(commit.committed_date).tm_year

                if(commit_year <= end and commit_year >=begin):
                        result_commits.append(commit)

	return result_commits

def getNumberOfFilesbyCommit(commit):
	repo.git.checkout(commit)
	print( sum([len(files) for r, d, files in os.walk(dir)]))

def getNumberOfFilesJavabyCommit(commit):
	repo.git.checkout(commit)
	counter=0
	for r, d, files in os.walk(dir):
		counter += len([file for file in files if file.endswith('.java')])
		
	print(counter)

	
def getNumberOfFilesJavaAllCommits():
	
	for commit in repo.iter_commits('master'):
		
		print commit.hexsha +": ",
		getNumberOfFilesJavabyCommit(commit)
	
def getNumberOfFilesAllCommits():
	
	for commit in repo.iter_commits('master'):
		print commit.hexsha +": ",
		getNumberOfFilesbyCommit(commit)

def fileLen(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
		return i+1

def countJavaLines(commit):
	repo.git.checkout(commit)
	len_java = 0
	for r, d, files in os.walk(dir):
		for file in files:
			if file.endswith('.java'):
				len_java += fileLen(r+'\\'+file)
	return len_java

def getNumberOfLinesJavaPerCommit():
	commitNumber = 1
	for commit in repo.iter_commits('master'):
		print commit.hexsha +": ", countJavaLines(commit)
		

def getNumberOfFilesPerYear(file_type=""):
	file_set = Set([])
	max_year = time.gmtime(all_commits[0].committed_date).tm_year
	
	year  = time.gmtime(all_commits[-1].committed_date).tm_year
	
	while year <= max_year:
		file_set = Set([])
		
		commits_year = get_all_commits_by_year_interval(all_commits,year,year)
		
		for commit in commits_year:
			repo.git.checkout(commit)
			for r, d, files in os.walk(dir):
				for file in files:
					if file_type == "":
						file_set.add(r+'\\'+file)
					elif file.endswith(file_type):
						file_set.add(r+'\\'+file)
						
		print("year:", str(year), str(len(file_set)))
		year += 1
		
	

def getNumberOfLinesJavaPerYear():
	
	repo.git.checkout(all_commits[0])
	counter = {}
	for commit in repo.iter_commits('master'):
		commit_date = time.gmtime(commit.committed_date)
		if commit_date.tm_year not in counter:
			counter[commit_date.tm_year] = 0
		for (file_name, stats) in commit.stats.files.items():
			if ".java" in file_name:
				counter[commit_date.tm_year] += stats['lines']
	counter = collections.OrderedDict(sorted(counter.items()))
	printPerYear(counter)
	
def printPerYear(counter):
	for year,val in counter.items():
		print(str(year) +": "+ str(val))


print( "Questao 1")
getNumberOfFilesbyCommit(all_commits[1])
getNumberOfFilesbyCommit(all_commits[-1])

print( "Questao 2")
print( "primeiro")
getNumberOfFilesJavabyCommit(all_commits[1])
print ("ultimo")
getNumberOfFilesJavabyCommit(all_commits[-1])

print("Questao 3")
getNumberOfFilesAllCommits()

print("Questao 4")
getNumberOfFilesJavaAllCommits()

print("Questao 5")
getNumberOfLinesJavaPerCommit()


print("Questao 6")
getNumberOfFilesPerYear()

print("Questao 7")
getNumberOfFilesPerYear(".java")

print("Questao 8")
getNumberOfLinesJavaPerYear()