{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "GD2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNiD+iVr73xYZJBvc7YNEGC",
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
        "<a href=\"https://colab.research.google.com/github/nnh92/PLA/blob/main/Code_PLA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z_uOdLi4153m",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "outputId": "1e450afb-e5b3-4458-afcc-9975dbfa8041"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from scipy.spatial.distance import cdist\n",
        "\n",
        "means = [[2,2],[4,2]]\n",
        "cov =[[.3,.2],[.2,.3]]\n",
        "N = 20\n",
        "\n",
        "X0 = np.random.multivariate_normal(means[0], cov, N).T\n",
        "X1 = np.random.multivariate_normal(means[1], cov, N).T\n",
        "\n",
        "X = np.concatenate((X0,X1), axis = 1)\n",
        "y = np.concatenate((np.ones((1,N)), -1*np.ones((1,N))), axis = 1)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "plt.plot(X0[0,:],X0[1,:], 'b^', markersize = 5, alpha = .5)\n",
        "plt.plot(X1[0,:],X1[1,:], 'ro', markersize = 5, alpha = .5)\n",
        "plt.show()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}