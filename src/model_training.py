{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "O-z_Ti2ktDLS"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8) #80% data used for training(learning)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "QJoBRU7gumKn"
      },
      "outputs": [],
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "regression=LinearRegression() #we are activating our algorithm"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "iUS-Srt2wc56",
        "outputId": "0f233969-98e0-4a15-c722-f8fecc4de106"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
            ],
            "text/plain": [
              "LinearRegression()"
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "regression.fit(x_train,y_train) #.fit() used for training"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "0lOU2-_1yiRU"
      },
      "outputs": [],
      "source": [
        "y_pred=regression.predict(x_test)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gNl6D59W1bRD",
        "outputId": "d8276edf-89f5-443b-fc5b-ec2b2d719a6e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[14619.19514813  3911.98960573 11192.94217386  5092.95188616\n",
            "  7625.58920072 14640.97814891 13702.10288258  4754.38919822\n",
            "  3834.75784148 14673.23174429  4877.92292701  9329.1108284\n",
            " 28441.72818652  5258.74458086 11587.90406818  4317.16479462\n",
            "  7686.20438703 15363.31341947 27799.95250382  8202.60411089\n",
            " 13975.2464654   1184.41881521  3998.59622018  9155.39030482\n",
            " 18030.05038336 15459.86623784 33598.34337726  6120.54275168\n",
            "  9364.22111203 12939.10796694  7730.4359391  11334.3848769\n",
            " 34713.45686953 14171.94701641 12715.89755342 10822.94010976\n",
            "  8786.09982863  2244.94705176 29338.1644626   6172.1030978\n",
            " 12395.19455119  6341.36515564  9934.96322613  6415.98021706\n",
            "  8284.04067168  8749.8346777  11177.43196916 14208.49364881\n",
            " 12357.77090216  5446.18633442  9966.47733388 12937.1003519\n",
            " 32012.59985506  9337.22944161  9292.09664773  6228.0590248\n",
            "  6256.70214093 14830.93476848 11187.74785131  2486.71759922\n",
            " 29132.68692206 14666.09260413 30224.59169362  9355.65921944\n",
            "  8413.21317656  8315.6708759   7184.61749588  2490.38733252\n",
            " 27021.00292995  6682.13937217 14470.14221329  9283.19284546\n",
            " 11765.72801861  7275.51719107 25981.72621804  -188.03539031\n",
            " 10462.98595523 15184.48568338 10411.98502866  6585.07930284\n",
            " 28346.81330496 25439.37359459 12266.45219648  9583.3280987\n",
            " 11590.12673644 11765.57693698  5959.16999418 13043.05228935\n",
            "  4789.37271283  6052.17626117 13382.61876295  5253.47552673\n",
            " 15587.50221932 31888.74965963  6331.90197752  8140.79194165\n",
            " 27252.07720075 12167.27204645 40030.72246986 13744.4151038\n",
            "  4291.25046729  5430.54931698  2545.27550227  1662.57121615\n",
            " 15231.00274487  8821.05790019 11855.4728465  11004.73954385\n",
            " 36892.07095967  6209.09418374  9726.14430935 36657.85851914\n",
            " 12869.05387139  7337.51664499 33517.02291294  9689.84054244\n",
            "  7024.99509713 12273.69270634 12741.25133075  8937.04423832\n",
            " 10822.4050028  11706.0140741  11471.42119535  7225.56976212\n",
            "   335.63024273  7728.55518052 11298.29620694 37438.06550416\n",
            "  8621.34594847  7551.82325623  3486.65491834  8146.86682421\n",
            " 11591.13052211  3177.0529436  14325.10333438 10953.02811609\n",
            " 33276.25615114 11379.83531157  5827.13834439 10640.84847792\n",
            " 25320.66805349 28987.80029894 34054.16691047  7316.01149487\n",
            " 10607.50285639 39879.25725658 34872.58268987 30715.28151454\n",
            "  1977.93877972  9654.92104314 12040.16758483  1647.7086715\n",
            "  9612.95068788  9389.19449486 10097.15015912 -1111.74477457\n",
            "  6500.45244744 10926.94844748 11078.6819693  10846.57968767\n",
            " 13073.48905402  8586.29963643  3512.13555213 32017.3652016\n",
            "  3468.88347311 29148.29967061  8040.86163144  8741.75572346\n",
            " 10220.06054047 13153.85785755  5723.95372427 -1165.90822718\n",
            " 26506.67361856  1917.60148778 10890.83550863  6348.04628965\n",
            " 15534.77274625 28211.77384156  2219.14882089  3507.84247139\n",
            "  3333.15669069 11925.50149899 11740.24742854 10653.51266691\n",
            " 11032.79897152 38485.86912349 12211.09534803 12435.75282658\n",
            "  5698.11696486  8715.38385711  2217.3320339  10617.85372371\n",
            " 10205.08185563  2125.73425969 12905.50871993  2308.14348861\n",
            " 27639.04842503  1826.91684581  7908.57635616  6697.26913864\n",
            "   464.92956036 15678.12402013  2123.8291885  12370.83025616\n",
            "  7188.43831082  9388.29320932  4548.03468475 12657.99798298\n",
            "  5817.61119468  5747.49075833 18001.05114161 40673.47412594\n",
            "  -981.59392708   981.20251519 14498.69704522  1683.82274079\n",
            "  9171.59858854  7758.45925117 11159.25227344 11578.18726457\n",
            " 12774.97743422 33676.56816717 28560.68739682 29156.88583209\n",
            " 35622.91346023  6495.90574122 15478.51461227 13452.11585187\n",
            "  4170.03123434 14890.96517962  -621.67834481 17223.51006052\n",
            "   696.16917244 12738.08889214 33329.50760195  8286.54482141\n",
            "  8165.61419912 17187.24486587  3044.86908174  7023.61087324\n",
            "  6696.98765717 36926.40568379  8507.87447635 33240.27002503\n",
            " 13388.89518985  5084.14708436 34143.78138225  8462.24506033\n",
            " 32791.86702601 13971.74211709  5540.3510558  -2342.45061413\n",
            " 11730.68170657  5178.05818025  8446.02610406  2697.896757\n",
            "  -310.81895892  9586.50484068 32586.42805772  9717.07512207\n",
            "  9894.22601312  6243.82285499  3571.54615921  3152.47359534\n",
            " 34865.62011811 17100.01490398  3996.96908708 18539.95984498]\n"
          ]
        }
      ],
      "source": [
        "print(y_pred)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
