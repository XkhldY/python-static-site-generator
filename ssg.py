import typer
from ssg.site import Site


def main(source='content', dest='dist'):
    config = {'source': source, 'dest': dest}
    site = Site(**config)
    site.build()


typer.run(main)
