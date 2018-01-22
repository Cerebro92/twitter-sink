import click

from app.utils import twitter_driver

@click.command()
@click.argument('search_text')
def sink(search_text):
    status = twitter_driver(search_text)
    click.echo('sinked : %s' % status)

if __name__ == '__main__':
    sink()
