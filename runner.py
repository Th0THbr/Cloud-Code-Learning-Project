import subprocess

def build_cmd(filename):
	if (filename.endswith(".py")):
		return ["python", filename]
	elif (filename.endswith(".java")):
		classname = filename.replace(".java", "")
		return [["javac", filename],["java", classname]]
			
	raise ValueError("Unsupported File type")
		

def jobber(cmds):
	result = None
	try:
		for cmd in cmds:
			result=subprocess.run(
				cmd, 
				capture_output=True, 
				text=True, 
				timeout=2
				)
		if(result.returncode!=0):
			break

except subprocess.TimeoutExpired:
	return {"verdict": "TIMEOUT"}
except Exception as e:
	return {"INTERNAL ERROR": str(e)}

	return{
		"verdict":( "OK" if result.returncode==0 else "RUNTIME_ERROR"),
		"error": result.stderr,
		"output": result.stdout,
		"exit_code": result.returncode
		}


output=jobber(build_cmd("example.java"))
print(output)
