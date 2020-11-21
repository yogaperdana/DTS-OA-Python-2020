priority = 0
email = 'yogapp@gmail.com'

def isPointInCircle(x, y, r, center=(0, 0)):
	return (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r ** 2

import random
def generateRandomSquarePoints(n, length, center=(0, 0)):
	minx = center[0] - length / 2
	miny = center[1] - length / 2
	maxx = center[0] + length / 2
	maxy = center[1] + length / 2
	return [[random.uniform(minx, maxx), random.uniform(miny, maxy)] for i in range(n)]

def MCCircleArea(r, n=100, center=(0,0)):
	sp = generateRandomSquarePoints(n, r*2, center)
	cp = [[pt[0], pt[1]] for pt in sp if isPointInCircle(pt[0], pt[1], r, center)]
	return (r * 2) ** 2 * (len(cp) / len(sp))

def LLNPiMC(nsim, nsample):
	sd = [MCCircleArea(1, nsample) for i in range(nsim)]
	return sum(sd) / len(sd)

def relativeError(act, est):
	return abs((est - act) / act) * 100
