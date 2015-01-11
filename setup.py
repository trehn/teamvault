from setuptools import setup, find_packages

setup(
    name="teamvault",
    version="0.2.0",
    description="Keep your passwords behind the firewall",
    author="Torsten Rehn",
    author_email="torsten@rehn.email",
    license="GPLv3",
    url="https://github.com/trehn/teamvault",
    package_dir={'': "src"},
    packages=find_packages("src"),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "teamvault=teamvault.cli:main",
        ],
    },
    keywords=["password", "safe", "manager", "sharing"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business",
        "Topic :: Security",
    ],
    install_requires=[
        "cryptography == 0.6.1",
        "dj-static == 0.0.6",
        "Django == 1.7.2",
        "django-filter == 0.7",
        "django-gravatar2 == 1.1.4",
        "djangorestframework == 3.0.3",
        "gunicorn == 19.1.1",
        "psycopg2 == 2.5.4",
        "pytz == 2014.10",
        #"hg+https://bitbucket.org/kavanaugh_development/django-auth-ldap@python3-ldap",
    ],
    zip_safe=False,
)
