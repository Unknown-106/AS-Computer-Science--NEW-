Imports System
Imports System.Transactions

Module Module1

    'Doubling'
    Sub Doubling(ByVal num As Integer)
        num *= 2
        Console.WriteLine("Inside subroutine: " & num)
    End Sub

    'Swap'
    Sub Swap(ByRef a As Integer, ByRef b As Integer)
        Dim temp As Integer
        temp = a
        a = b
        b = temp
    End Sub


    'ApplyDiscount'
    Sub ApplyDiscount(ByVal price As Integer, ByVal discount As Decimal)
        Console.WriteLine("Discount: " & discount & "%")
        price = price * (1 - discount / 100)
        Console.WriteLine("Discounted Price: " & price)
    End Sub


    'AddBonus'
    Sub AddBonus(ByRef salary As Integer, ByVal bonus As Integer)
        salary += bonus
    End Sub


    'SwapNames'
    Sub SwapNames(ByRef name1 As String, ByRef name2 As String)
        Dim temp As String
        temp = name1
        name1 = name2
        name2 = temp
    End Sub


    Sub Main()


        'Doubling'
        Dim number As Integer = 10
        Doubling(number)
        Console.WriteLine("After subroutine: " & number)


        'Swap'
        Dim x As Integer = 5
        Dim y As Integer = 9
        Console.WriteLine("Before: x = " & x & ", y = " & y)
        Swap(x, y)
        Console.WriteLine("After: x = " & x & ", y = " & y)


        'ApplyDiscount'
        Dim price As Integer = 50
        Dim discount As Decimal = 10
        Console.WriteLine("Start Price: " & price)
        ApplyDiscount(price, discount)
        Console.WriteLine("Original Price: " & price)


        'AddBonus'
        Dim salary As Integer = 25000
        Dim bonus As Integer = 5000
        Console.WriteLine("Current Salary: " & salary)
        Console.WriteLine("Bonus: " & bonus)
        AddBonus(salary, bonus)
        Console.WriteLine("New Salary: " & salary)


        'SwapNames'
        Dim name1 As String = "Bob"
        Dim name2 As String = "Alice"
        Console.WriteLine("Before swap: " & name1 & "and " & name2)
        SwapNames(name1, name2)
        Console.WriteLine("After swap: " & name1 & "and " & name2)


    End Sub


End Module