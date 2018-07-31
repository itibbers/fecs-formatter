import os
import platform
import sublime
import sublime_plugin

class FecsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print('fecs start:')
        fileName = self.view.file_name()
        print(fileName)
        os.system('fecs format ' + fileName + ' --replace')
        print('fecs end.')
