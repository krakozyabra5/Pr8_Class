using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laba_4
{
    internal class Program
    {
        static int CountOddNumbers(int[] arr)
        {
            int count = 0;
            foreach (var num in arr)
            {
                if (num % 2 != 0)
                {
                    count++;
                }
            }
            return count;

        }
        static void Main(string[] args)
        {
            int n = 5; // Размер массива, можете задать любое другое значение
            int[] B = new int[n];

            // Заполнение массива B значениями, введёнными пользователем
            for (int i = 0; i < n; i++)
            {
                Console.Write($"Введите элемент B[{i}]: ");
                B[i] = Convert.ToInt32(Console.ReadLine());
            }

            int d = CountOddNumbers(B);
            Console.WriteLine($"Количество нечётных элементов в массиве: {d}");
        }

      
    }
}
