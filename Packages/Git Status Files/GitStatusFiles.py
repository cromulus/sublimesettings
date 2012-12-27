import sublime, sublime_plugin, os, commands, re, array, string

class GitStatusFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        views =  sublime.active_window().views()
        if len(views) < 1:
            sublime.error_message("You have to open a file in the git repository.")
        current_path = os.path.abspath(os.path.join(views[0].file_name(), '..'))
        os.chdir(current_path)
        status_lines = commands.getoutput("git status --porcelain").split('\n')
        for item in status_lines:
            file_name = re.sub(r'(.*\s)', '', item)
            path = os.path.join(os.getcwd(), file_name)
            sublime.active_window().open_file(path)