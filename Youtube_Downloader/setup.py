from cx_Freeze import setup, Executable

includefiles = ["Img1.ico", "Youtube_logo.png"]

setup(

	name="MvYtoutube",
	version="2.5",
	description="version Linux",
	executables=[Executable("YouTube.py", icon="Img1.ico")],
	option = {
	    'buil_exe': {
	        'include_files' : includefiles
	    }
	}
)
