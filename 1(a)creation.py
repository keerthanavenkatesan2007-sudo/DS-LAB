{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMkR/RdFguyg3tJdlF8ozRw",
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
        "<a href=\"https://colab.research.google.com/github/keerthanavenkatesan2007-sudo/DS-LAB/blob/main/1(a)creation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T2ihdeqTRSFm",
        "outputId": "01671e29-c287-4f19-9606-06405934e4f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sun\n",
            "mon\n",
            "tue\n",
            "wed\n"
          ]
        }
      ],
      "source": [
        "class node:\n",
        "  def __init__(self,dataval=None):\n",
        "      self.dataval=dataval\n",
        "      self.nextval=None\n",
        "class slinkedlist:\n",
        "  def __init__(self):\n",
        "      self.headval=None\n",
        "  def listprint(self):\n",
        "      printval=self.headval\n",
        "      while printval is not None:\n",
        "           print (printval.dataval)\n",
        "           printval=printval.nextval\n",
        "  def atbeginning(self,newdata):\n",
        "    newnode=node(newdata)\n",
        "    newnode.nextval=self.headval\n",
        "    self.headval=newnode\n",
        "\n",
        "list_obj=slinkedlist()\n",
        "list_obj.headval=node(\"mon\")\n",
        "e2=node(\"tue\")\n",
        "e3=node(\"wed\")\n",
        "list_obj.headval.nextval=e2\n",
        "e2.nextval=e3\n",
        "list_obj.atbeginning(\"sun\")\n",
        "list_obj.listprint()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class node:\n",
        "  def __init__(self,data):\n",
        "       self.data = data\n",
        "       self.next = None\n",
        "\n",
        "class linkedlist:\n",
        "  def __init__(self):\n",
        "       self.head = None\n",
        "\n",
        "  def push(self,new_data):\n",
        "      new_node=node(new_data)\n",
        "      new_node.next=self.head\n",
        "      self.head=new_node\n",
        "\n",
        "  def insertafter(self,prev_node,new_data):\n",
        "   if prev_node is None:\n",
        "     print(\"The given previous node must be in linked list.\")\n",
        "     return\n",
        "   new_node=node(new_data)\n",
        "   new_node.next=prev_node.next\n",
        "   prev_node.next=new_node\n",
        "\n",
        "  def append(self,new_data):\n",
        "    new_node=node(new_data)\n",
        "    if self.head is None:\n",
        "      self.head=new_node\n",
        "      return\n",
        "    last=self.head\n",
        "    while(last.next):\n",
        "      last=last.next\n",
        "    last.next=new_node\n",
        "\n",
        "  def printlist(self):\n",
        "    temp=self.head\n",
        "    while(temp):\n",
        "      print(temp.data)\n",
        "      temp=temp.next\n",
        "\n",
        "if __name__=='__main__':\n",
        "      llist=linkedlist()\n",
        "      llist.append(6)\n",
        "      llist.push(7)\n",
        "      llist.push(1)\n",
        "      llist.append(4)\n",
        "      llist.insertafter(llist.head.next,8)\n",
        "      print('Created linked list is:')\n",
        "      llist.printlist()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2CURdLOZX_OC",
        "outputId": "e431a185-adbb-4ae2-b863-850c5b94c812"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Created linked list is:\n",
            "1\n",
            "7\n",
            "8\n",
            "6\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BJNpsv8kYpdh"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}