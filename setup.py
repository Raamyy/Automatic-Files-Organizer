from distutils.core import setup
setup(
  name = 'organise_files',         # How you named your package folder (MyLib)
  packages = ['organise_files'],   # Chose the same as "name"
  include_package_data=True,
  version = '0.1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple python utility that helps in organizing your folders',   # Give a short description about your library
  author = 'Ramy Gamal',                   # Type in your name
  author_email = 'ramyeg26@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Raamyy/Automatic-Files-Organizer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Raamyy/Automatic-Files-Organizer/archive/0.1.2.tar.gz',    # I explain this later on
  keywords = ['Cleaning', 'Organising', 'Organizing','Files','Folders'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
  entry_points = {
        'console_scripts': ['organise_files=organise_files.cli:main'],
    }
)