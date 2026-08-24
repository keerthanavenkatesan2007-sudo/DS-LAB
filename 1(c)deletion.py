{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMvQF0Wdncn9y9f3Z0Q9t2n",
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
        "<a href=\"https://colab.research.google.com/github/keerthanavenkatesan2007-sudo/DS-LAB/blob/main/1(c)deletion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "INSERTION\n"
      ],
      "metadata": {
        "id": "ogsQScIBgkf-"
      }
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
      "cell_type": "markdown",
      "source": [
        "CREATION\n"
      ],
      "metadata": {
        "id": "RJkfwzcBghSB"
      }
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
      "cell_type": "markdown",
      "source": [
        "DELETION\n"
      ],
      "metadata": {
        "id": "qwfKshTIgeDC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "  def __init__(self,data=None):\n",
        "    self.data=data\n",
        "    self.next=None\n",
        "\n",
        "class Slinkedlist:\n",
        "    def __init__(self):\n",
        "          self.head=None\n",
        "\n",
        "    def atbeginning(self,data_in):\n",
        "      newnode=Node(data_in)\n",
        "      newnode.next=self.head\n",
        "      self.head=newnode\n",
        "\n",
        "    def removenode(self,removekey):\n",
        "      headval = self.head\n",
        "\n",
        "      # If head node itself holds the key to be removed\n",
        "      if headval is not None and headval.data == removekey:\n",
        "          self.head = headval.next\n",
        "          return\n",
        "\n",
        "      # Search for the key to be removed, keep track of the previous node\n",
        "      prev = None\n",
        "      while headval is not None and headval.data != removekey:\n",
        "          prev = headval\n",
        "          headval = headval.next\n",
        "\n",
        "      # If key was not present in linked list\n",
        "      if headval is None:\n",
        "          return\n",
        "\n",
        "      # Unlink the node from linked list\n",
        "      if prev is not None:\n",
        "          prev.next = headval.next\n",
        "\n",
        "    def LListprint(self):\n",
        "         printval = self.head\n",
        "         while (printval):\n",
        "             print(printval.data)\n",
        "             printval = printval.next\n",
        "\n",
        "llist = Slinkedlist()\n",
        "llist.atbeginning(\"Mon\")\n",
        "llist.atbeginning(\"Tue\")\n",
        "llist.atbeginning(\"Wed\")\n",
        "llist.atbeginning(\"Thu\")\n",
        "llist.removenode(\"Tue\")\n",
        "print(\"Linked list after removing 'Tue':\")\n",
        "llist.LListprint()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BJNpsv8kYpdh",
        "outputId": "b4363f1d-d332-4cfa-db03-2bfc00f9071b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Linked list after removing 'Tue':\n",
            "Thu\n",
            "Wed\n",
            "Mon\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "TRAVERSAL\n"
      ],
      "metadata": {
        "id": "8DOP5lAXgYwD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self,data):\n",
        "         self.data=data\n",
        "         self.next=None\n",
        "\n",
        "class LinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def printList(self):\n",
        "        temp = self.head\n",
        "        while (temp):\n",
        "            print(temp.data)\n",
        "            temp = temp.next\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    llist = LinkedList()\n",
        "\n",
        "    llist.head = Node(1)\n",
        "    second = Node(2)\n",
        "    third = Node(3)\n",
        "\n",
        "    llist.head.next = second\n",
        "    second.next = third\n",
        "\n",
        "    llist.printList()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "adv1k5SfedZQ",
        "outputId": "4108d503-17e3-46f9-e80d-f795801fdb34"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ]
    }
  ]
}