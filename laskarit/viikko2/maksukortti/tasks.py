from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def test(ctx):
    ctx.run("pytest src")
