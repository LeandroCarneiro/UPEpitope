using ConsoleApp.AppObjects;
using ConsoleApp.Commanders;
using Tensorflow;

namespace ConsoleApp
{
    internal class Program
    {
        internal static readonly string[] batchNames = ["abcpred16.json"];

        static void Main(string[] args)
        {
            int option = 0;
            Console.WriteLine("Welcome to UPEpitope!");

            do
            {
                Console.WriteLine("Choose one of the option:");
                Console.WriteLine("1- Training model");
                Console.WriteLine("2- Predict epitope");
                Console.WriteLine("3- Print charts");
                Console.WriteLine("0- Save & Exit");
                
                if(!int.TryParse(Console.ReadLine(), out option))
                {
                    Console.Clear();
                    Console.WriteLine("Wrong option!");
                    continue;
                }

                switch (option)
                {
                    case 0:
                        Save();
                        continue;
                    case 1:
                        Train();
                        continue;
                    case 2:
                        Predict();
                        continue;
                    case 3:
                        Print();
                        continue;
                    default:
                        Console.WriteLine("Thanks!");
                        return;
                }

            } while (option == 0);
        }

        private static void Print()
        {
            throw new NotImplementedException();
        }

        private static AppResult[] Predict()
        {
            throw new NotImplementedException();
        }


        private static AppResult[] Train()
        {
            return new TrainCommander().Execute(batchNames);
        }

        private static AppResult[] Save()
        {
            throw new NotImplementedException();
        }
    }
}
