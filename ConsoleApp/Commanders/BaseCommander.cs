using ConsoleApp.AppObjects;

namespace ConsoleApp.Commanders
{
    public abstract class BaseCommander
    {
        public BaseCommander() { }

        public abstract AppResult[] Execute(string[] args);
    }
}
