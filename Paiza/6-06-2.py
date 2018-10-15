{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "157\n"
     ]
    }
   ],
   "source": [
    "# ループで合計を計算しよう\n",
    "\n",
    "points = {\"国語\" : 70, \"算数\" : 35, \"英語\" : 52}\n",
    "sum = 0\n",
    "# この下で、辞書の値の合計をループで計算してみよう\n",
    "\n",
    "#print(int(sum))\n",
    "#print(points)\n",
    "#print(points[\"国語\"])\n",
    "\n",
    "for (point,rank) in points.items():\n",
    "    sum += int(rank)\n",
    "    #print(sum)\n",
    "\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7]]\n"
     ]
    }
   ],
   "source": [
    "number = [[7 for i in range(4)] for j in range(5)]\n",
    "\n",
    "print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
