import os
import yaml

from flask import Flask as BaseFlask, Config as BaseConfig

class Config(BaseConfig):
	"""Extends the config class from flask to include YAML"""
	
	def from_yaml(self, config_file):
		with open(config_file) as f:
			c = yaml.load(f)			
			for item in c:
				if item.isupper():
					self[item] = c[item]
					
			
class Flask(BaseFlask):
	"""Extends Flask to get config file"""
	
	def make_config(self, instance_relative=False):
		root_path = self.root_path
		if instance_relative:
			root_path = self.instance_path
		return Config(root_path, self.default_config)
