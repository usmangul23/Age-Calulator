{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMFV4pFFoCHXa0Vv78yXDLv",
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
        "<a href=\"https://colab.research.google.com/github/usmangul23/Age-Calulator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_U9yPB31JQ0G"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Age Calculator"
      ],
      "metadata": {
        "id": "IZebOJM0Jbcc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime\n",
        "\n",
        "def calculate_age(birth_date):\n",
        "    # Get today's date\n",
        "    today = datetime.today()\n",
        "\n",
        "    # Calculate the difference in years, months, and days\n",
        "    years = today.year - birth_date.year\n",
        "    months = today.month - birth_date.month\n",
        "    days = today.day - birth_date.day\n",
        "\n",
        "    # Adjust for negative values in months and days\n",
        "    if days < 0:\n",
        "        months -= 1\n",
        "        days += (today - datetime(today.year, today.month, 1)).days\n",
        "\n",
        "    if months < 0:\n",
        "        years -= 1\n",
        "        months += 12\n",
        "\n",
        "    return years, months, days\n",
        "\n",
        "# Input: date of birth in 'YYYY-MM-DD' format\n",
        "dob_input = input(\"Enter your date of birth (YYYY-MM-DD): \")\n",
        "\n",
        "# Convert the input string to a datetime object\n",
        "dob = datetime.strptime(dob_input, \"%Y-%m-%d\")\n",
        "\n",
        "# Call the function to calculate the age\n",
        "years, months, days = calculate_age(dob)\n",
        "\n",
        "# Output the age\n",
        "print(f\"Your complete age is: {years} years, {months} months, and {days} days.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eoqTFpbnJgRY",
        "outputId": "d1d8c449-08c1-4c66-8e37-f3a7cd78055e"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your date of birth (YYYY-MM-DD): 1982-10-18\n",
            "Your complete age is: 42 years, 0 months, and 1 days.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Deploy this code to streamlit"
      ],
      "metadata": {
        "id": "Z2Z3sif0LUrN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from datetime import datetime\n",
        "\n",
        "# Streamlit app\n",
        "st.title(\"Age Calculator\")\n",
        "\n",
        "# Input: date of birth from the user\n",
        "dob_input = st.text_input(\"Enter your date of birth (YYYY-MM-DD):\")\n",
        "\n",
        "# Check if input is provided\n",
        "if dob_input:\n",
        "    try:\n",
        "        # Convert the input string to a datetime object\n",
        "        dob = datetime.strptime(dob_input, \"%Y-%m-%d\")\n",
        "\n",
        "        # Calculate the complete age\n",
        "        def calculate_age(birth_date):\n",
        "            today = datetime.today()\n",
        "            years = today.year - birth_date.year\n",
        "            months = today.month - birth_date.month\n",
        "            days = today.day - birth_date.day\n",
        "\n",
        "            if days < 0:\n",
        "                months -= 1\n",
        "                days += (today - datetime(today.year, today.month, 1)).days\n",
        "\n",
        "            if months < 0:\n",
        "                years -= 1\n",
        "                months += 12\n",
        "\n",
        "            return years, months, days\n",
        "\n",
        "        # Calculate age\n",
        "        years, months, days = calculate_age(dob)\n",
        "\n",
        "        # Display the result\n",
        "        st.success(f\"Your complete age is: {years} years, {months} months, and {days} days.\")\n",
        "\n",
        "    except ValueError:\n",
        "        st.error(\"Please enter a valid date in YYYY-MM-DD format.\")\n"
      ],
      "metadata": {
        "id": "cKIYZlPILZ7e"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}