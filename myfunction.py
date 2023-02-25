{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOoPqS2qwTEJjuDoAypR0Y8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yssuresh1981/Learning_ML/blob/main/myfunction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BUycnrrrxpJ1"
      },
      "outputs": [],
      "source": [
        "def average_list(num_list):\n",
        "  \n",
        "  num_sum=0\n",
        "\n",
        "  for i in range(0, len(num_list)):\n",
        "\n",
        "    num_sum=num_sum+num_list[i]\n",
        "\n",
        "  print('Average is:',num_sum/len(num_list))\n",
        "\n",
        "  return num_sum/len(num_list) "
      ]
    }
  ]
}