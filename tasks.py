"""Development tasks for django_push. Run with invoke."""
from invoke import task, run


# pylint: disable=unused-argument
@task(name='format')
def format_python(ctx):
    """Run python autoformating."""
    yapf_args = '--in-place --style=config/style.yapf'
    yapf_target = '--recursive django_push tasks.py'
    yapf_command = 'yapf ' + yapf_args + ' ' + yapf_target
    run(yapf_command)


@task(name='lint')
def lint_python(ctx):
    """Run python linting."""
    pylint_args = '--reports=n --rcfile=config/pylint.rc'
    pylint_target = 'django_push tasks.py'
    pylint_command = 'pylint ' + pylint_args + ' ' + pylint_target
    run(pylint_command)


@task(name='test')
def test_python(ctx):
    """Run python tests."""
    run('cd paragon && python manage.py test')
