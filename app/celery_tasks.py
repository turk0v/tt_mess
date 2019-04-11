from __init__ import celery
@celery.task()
def add_togethers(a, b):
	return a + b
