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
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "合計は113点です\n"
     ]
    }
   ],
   "source": [
    "# 学生メソッドを作る\n",
    "\n",
    "class Gakusei:\n",
    "    def __init__(self, kokugo, sansu):\n",
    "        self.kokugo = kokugo\n",
    "        self.sansu  = sansu\n",
    "\n",
    "    # この下に、合計得点を戻り値として返すsumメソッドを記述する\n",
    "    def sum(self):\n",
    "        return self.kokugo + self.sansu\n",
    "    \n",
    "yamada = Gakusei(70, 43)\n",
    "print(\"合計は\" + str(yamada.sum()) + \"点です\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello python\n"
     ]
    }
   ],
   "source": [
    "class Greeting:\n",
    "    def __init__(self):\n",
    "        self.msg = \"hello\"\n",
    "        self.target = \"paiza\"\n",
    "\n",
    "    def say_hello(self):\n",
    "        print(self.msg + \" \" + self.target)\n",
    "\n",
    "class Hello(Greeting):\n",
    "    # ここにオーバライドするメソッドを記述する\n",
    "    def say_hello(self , target):\n",
    "        print(self.msg + \" \" + target)\n",
    "\n",
    "    \n",
    "\n",
    "\n",
    "player = Hello()\n",
    "player.say_hello(\"python\")\n"
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
