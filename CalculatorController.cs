using BasicCalculator.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace BasicCalculator.Controllers
{
    public class CalculatorController : Controller
    {
        // GET: Calculator
        public ActionResult Index()
        {
            return View(new Calculator());
        }

        [HttpPost]

        public ActionResult Index(Calculator c,String calculate)
        {
           if(calculate == "add")
            {
                c.TotalNum = c.FirstNum + c.SecondNum;
            }
            else if (calculate == "min")
            {
                c.TotalNum = c.FirstNum - c.SecondNum;
            }
            else if (calculate == "mul")
            {
                c.TotalNum = c.FirstNum * c.SecondNum;
            }
            else
            {
                c.TotalNum = c.FirstNum / c.SecondNum;
            }

            return View(c);
        }

    }
}