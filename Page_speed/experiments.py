__author__ = 'jnejati'

from chromium_driver import *
import modifications as modify
import apache_conf
import os
from urllib.parse import urlparse



class SetExperiment():

    def __init__(self, exp_type):
        self.exp_type = exp_type

    def run(self, my_site, profile):
        if self.exp_type == 'compression':
            os.system('cp -R /var/www/original.testbed.localhost/*  /var/www/modified.testbed.localhost/')
            my_exp = modify.Compression()
            my_exp.enable()
            apache_conf.ApacheConf.restart_apache()
            my_run = RunChromium(my_site, 'modified', profile)
            my_run.main_run()
            my_exp.disable()
            apache_conf.ApacheConf.restart_apache()

        elif self.exp_type == 'minification':
            os.system('cp -R /var/www/original.testbed.localhost/*  /var/www/modified.testbed.localhost/ ')
            my_exp = modify.Minification('/var/www/modified.testbed.localhost', my_site)

            output_file = '/home/shreya/page_speed/' + '/' + 'minification_result.txt'
            my_exp.minify(output_file)
            print('chromium inside minify run')
            my_run = RunChromium(my_site, 'modified', profile)
            my_run.main_run()

        elif self.exp_type == 'inline':
            os.system('cp -R /var/www/original.testbed.localhost/*  /var/www/modified.testbed.localhost/ ')
            print('Original copied to modified.')
            my_exp = modify.Inline('/var/www/modified.testbed.localhost/', 'http://modified.testbed.localhost', my_site)
            my_exp.inliner()
            my_run = RunChromium(my_site, 'modified', profile)
            my_run.main_run()
