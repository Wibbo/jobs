"""
Reads details from the application configuration file and presents them appropriately as application parameters.
"""

import configparser
import json
import numpy as np


class AppConfig:

    @staticmethod
    def string_to_boolean(parameter_value, parameter_name='Invalid entry'):

        if parameter_value == 'True':
            return True
        elif parameter_value == 'False':
            return False
        else:
            err_msg = f'The value of {parameter_name} in the GoL ini file is {parameter_value}. '
            err_msg += f'It must be either True or False. The application cannot continue.'
            raise KeyError(err_msg)

    @staticmethod
    def validate_setting(value, min_val, max_val):
        if min_val > max_val:
            raise KeyError

        if value < min_val:
            value = min_val
        elif value > max_val:
            value = max_val

        return value

    @staticmethod
    def file_exists(file_name):
        f = None

        try:
            f = open(file_name)
        except Exception as e:
            raise e
        finally:
            if f is not None:
                f.close()

    def __init__(self, cfg_file):
        """
        Constructor for the AppConfig class.
        Reads parameters from the specified configuration file
        and presents them appropriately to the application.
        :param cfg_file: The name of the configuration file to read.
        """
        AppConfig.file_exists(cfg_file)

        cfg = configparser.ConfigParser()
        cfg.read(cfg_file)

        self.urlList = cfg.items('ITJOBS')
        self.max_sectors = int(cfg['GENERAL']['max_sectors'])





        # jobs_watch_url_1
        '''
        self. = int(cfg['GRID']['number_of_rows'])
        self.row_count = AppConfig.validate_setting(self.row_count, 2, 400)

        self.column_count = int(cfg['GRID']['number_of_columns'])
        self.column_count = AppConfig.validate_setting(self.column_count, 2, 500)

        self.info_bar_width = int(cfg['GRID']['info_bar_width'])
        self.info_bar_width = AppConfig.validate_setting(self.info_bar_width, 0, 300)

        self.screen_width_from_ini = int(cfg['GRID']['screen_width'])
        self.screen_width_from_ini = AppConfig.validate_setting(self.screen_width_from_ini, 200, 2400)

        self.show_cell_counts = cfg['ACTIONS']['show_cell_counts']
        self.show_cell_counts = AppConfig.string_to_boolean(self.show_cell_counts, 'cell counts')

        self.screen_height_from_ini = int(cfg['GRID']['screen_height'])
        self.screen_height_from_ini = AppConfig.validate_setting(self.screen_height_from_ini, 200, 1024)

        self.cell_reproduction_rule = int(cfg['ACTIONS']['cell_reproduction_rule'])
        self.cell_reproduction_rule = AppConfig.validate_setting(self.cell_reproduction_rule, 1, 3)

        self.live_cell_percentage = int(cfg['GRID']['live_cell_percentage'])
        self.live_cell_percentage = AppConfig.validate_setting(self.live_cell_percentage, 0, 100)
        self.dead_cell_percentage = 100. - self.live_cell_percentage

        self.grid_width = self.screen_width_from_ini - self.info_bar_width
        self.grid_height = self.screen_height_from_ini

        self.cell_width = int(self.grid_width / self.column_count)
        self.cell_height = int(self.grid_height / self.row_count)

        self.grid_width = int(self.cell_width * self.column_count)
        self.grid_height = int(self.cell_height * self.row_count)

        self.window_width = int(self.cell_width * self.column_count) + self.info_bar_width + 1
        self.window_height = int(self.cell_height * self.row_count) + 1

        self.grid_colour = json.loads(cfg['COLOUR']['grid_lines'])
        self.active_cell_colour = json.loads(cfg['COLOUR']['active_cell_colour'])
        self.inactive_cell_colour = json.loads(cfg['COLOUR']['inactive_cell_colour'])

        self.draw_grid = cfg['GRID']['draw_grid']

        self.draw_grid = AppConfig.string_to_boolean(self.draw_grid, 'draw_grid')

        self.clock_ticks = int(cfg['TIMING']['ticks_per_second'])
        self.clock_ticks = AppConfig.validate_setting(self.clock_ticks, 1, 400)
        '''



