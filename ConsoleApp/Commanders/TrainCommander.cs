using ConsoleApp.AppObjects;
using ConsoleApp.Entities;

namespace ConsoleApp.Commanders
{
    public class TrainCommander : BaseCommander
    {
        public override AppResult[] Execute(string[] batchNames)
        {
            foreach (var batchName in batchNames)
            {
                var allEpitopes = ReadBatch(batchName);

            }
            return new AppResult[0];
        }

        private Epitope[] ReadBatch(string batchName)
        {
            throw new NotImplementedException();
        }
    }
}
