{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOtHjkjntgg+/QBNCtCjq08",
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
        "<a href=\"https://colab.research.google.com/github/bingxiaochen/ST554/blob/main/ST_554_HW6_Part_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "HoiDrWEfKqrN"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from numpy.random import default_rng\n",
        "from sklearn import linear_model\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "class slr_slope_simulator:\n",
        "\n",
        "\n",
        "    def __init__(self, beta_0, beta_1, x, sigma, seed):\n",
        "        self.beta_0 = beta_0\n",
        "        self.beta_1 = beta_1\n",
        "        self.sigma = sigma\n",
        "        self.x = np.asarray(x)\n",
        "\n",
        "        self.n = len(self.x)\n",
        "        self.rng = np.random.default_rng(seed)\n",
        "        self.slopes = []\n",
        "\n",
        "    # Generate one dataset\n",
        "    def generate_data(self):\n",
        "        eps = self.rng.normal(0, self.sigma, self.n)\n",
        "        y = self.beta_0 + self.beta_1 * self.x + eps\n",
        "        return self.x, y\n",
        "\n",
        "    # Fit simple linear regression and return slope\n",
        "    def fit_slope(self, x, y):\n",
        "        model = LinearRegression()\n",
        "        model.fit(x.reshape(-1, 1), y)\n",
        "        return model.coef_[0]\n",
        "\n",
        "    # Run many simulations\n",
        "    def run_simulations(self, n_sims):\n",
        "\n",
        "        slopes = []\n",
        "\n",
        "        for _ in range(n_sims):\n",
        "\n",
        "            x, y = self.generate_data()\n",
        "            slope_hat = self.fit_slope(x, y)\n",
        "\n",
        "            slopes.append(slope_hat)\n",
        "\n",
        "        self.slopes = np.array(slopes)\n",
        "\n",
        "    # plot the sampling distribution\n",
        "    def plot_sampling_distribution(self):\n",
        "\n",
        "        if len(self.slopes) == 0:\n",
        "            raise Exception(\"Call run_simulations() first!\")\n",
        "            return\n",
        "\n",
        "        plt.hist(self.slopes, bins=20)\n",
        "        plt.xlabel(\"Slope\")\n",
        "        plt.ylabel(\"Frequency\")\n",
        "        plt.show()\n",
        "\n",
        "    def find_prob(self, value, sided):\n",
        "        if len(self.slopes) == 0:\n",
        "            raise Exception(\"Call run_simulations() first!\")\n",
        "            return\n",
        "\n",
        "        if sided == \"above\":\n",
        "            return np.mean(self.slopes > value)\n",
        "        elif sided == \"below\":\n",
        "            return np.mean(self.slopes < value)\n",
        "        elif sided == \"two-sided\":\n",
        "            return 2 * np.mean(np.abs(self.slopes) > abs(value))\n",
        "\n",
        "        else:\n",
        "            raise Exception(\"sided must be 'above', 'below', or 'two-sided'\")\n",
        "\n",
        "\n",
        "    @property\n",
        "    def slope(self) -> float:\n",
        "        \"\"\"Return the mean of the simulated slopes\"\"\"\n",
        "        if len(self.slopes) == 0:\n",
        "            raise Exception(\"Call run_simulations() first!\")\n",
        "            return None\n",
        "\n",
        "        return np.mean(self.slopes)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Test the class and its methods\n",
        "sim = slr_slope_simulator(beta_0 = 12,\n",
        "                    beta_1 = 2,\n",
        "                    x = np.array(list(np.linspace(start = 0, stop = 10, num = 11))*3),\n",
        "                    sigma = 1,\n",
        "                    seed = 10)"
      ],
      "metadata": {
        "id": "h4U4fpVGPKpe"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# call the plot without simulations -- should return error message\n",
        "sim.plot_sampling_distribution()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 287
        },
        "id": "AQxmtUGpPka0",
        "outputId": "37f9afa4-2a2f-4e46-f807-033bc7bdead2"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "Exception",
          "evalue": "Call run_simulations() first!",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mException\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_189/1619506736.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# call the plot without simulations -- should return error message\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0msim\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplot_sampling_distribution\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/tmp/ipykernel_189/2059495106.py\u001b[0m in \u001b[0;36mplot_sampling_distribution\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mslopes\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 50\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Call run_simulations() first!\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     51\u001b[0m             \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mException\u001b[0m: Call run_simulations() first!"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# run 10000 simulations\n",
        "sim.run_simulations(10000)"
      ],
      "metadata": {
        "id": "bnAmzbpyQDWs"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Plot the sampling distribution\n",
        "sim.plot_sampling_distribution()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "I0ig0H-9Q7Qn",
        "outputId": "9310858b-3ded-4b29-9ac1-14f9f867ecbb"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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nDmja6+9VvPmzav3mwgk6fXXX9ekSZM0a9Ys7d69W7169VJCQoJKSkrcNUod7ppNkrp37+603z7++GN3jPCDGjLb5s2bdd9992nTpk3KyclRVFSUBg0apG+++cZR4/afOQNeJclYs2bNj9bMnz/fuPbaa52WZWZmGj/5yU8cz3/7298aQ4cOdaqJjY01/vCHP7is18vlqtmWLVtmWK1WN3TYcJcyW1xcnDF58mSnZZMmTTL69evneO6L+80wXDefL+67kpISQ5KxZcuWH6y52H6pra01IiIijPnz5zvWnzp1yggMDDRee+019zR+iVwxn2EYRnJysjF8+HB3tdkglzLbf+rYsaPx7LPP1lnet29fIzU11fG8pqbGiIyMNNLT013V6mVz1WyzZs0yevXq5drmrtDlzmYYhnHu3DmjZcuWxvLlyw3D8MzPHEeIGoG4uDgVFhbq3XfflWEYKi4u1t///ncNGTLEUZOTk6P4+Hin1yUkJCgnJ8fT7V6WS5lNksrLy9WxY0dFRUVp+PDhysvL81LHl66ysrLOx0PBwcHasWOHqqurJTXe/SZd2nyS7+27srIySVLr1q1/sOZi++Xo0aOy2WxONVarVbGxsV7fd66Y74LNmzcrLCxMXbp00cMPP1znY3pPu5TZLqaqqkq5ublO8/v5+Sk+Pt6r+84Vs11w+PBhRUZG6tprr1VSUpIKCgqueJtXoiGznTlzRtXV1Y7XeOJnjkDUCPTr108rV67Uvffeq4CAAEVERMhqtTp9tGGz2ercdTs8PFw2m83T7V6WS5mtS5cuWrp0qf75z3/qlVdeUW1trW677TYdP37ci51fXEJCgv72t78pNzdXhmFo165d+tvf/qbq6mr961//ktR495t0afP52r6rra3VhAkT1K9fP914440/WHex/XLhn76271w1n3T+47IVK1Zow4YNevrpp7VlyxbdfffdqqmpcVv/P+ZSZ7uYf/3rX6qpqfGpfeeq2SQpNjZWWVlZWr9+vRYtWqSjR4+qf//+On36tIu6vTwNnW3q1KmKjIx0BCBP/MyZ5qs7GrODBw9q/PjxmjlzphISElRUVKQpU6booYce0ssvv+zt9q7IpcwWFxfn9CW8t912m7p27aq//vWvmjt3rrdav6gZM2bIZrPp1ltvlWEYCg8PV3JysjIyMuTn1/j/LnIp8/navktN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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Approximate the two-sided probability of being larger than 2.1\n",
        "sim.find_prob(2.1,\"two-sided\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Eu0hg3E2RJ3U",
        "outputId": "3cad0ef4-d75f-40e2-bea7-cedcb0486e15"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.float64(0.0704)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Print out the value of the simulated slopes\n",
        "sim.slope\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hzPizFvhRW3k",
        "outputId": "c8cb17b1-eea3-4eba-a02f-295458179745"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.float64(2.0001514298546166)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "KClCadsUSrlA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}