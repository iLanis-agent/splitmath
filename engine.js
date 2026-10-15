var SplitMath = (function () {
  function num(x) { return typeof x === "number" && isFinite(x); }
  function pos(x) { return num(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function jsnum(x) { if (typeof x === "number" && isFinite(x) && x === Math.trunc(x)) return String(Math.trunc(x)); return String(x); }
  var LOAD = 1.4, EFF = 0.8, VOLTS = 120, W_PER_HP = 746;
  function tonnagePlan(diameter, factor, rating) {
    if (!pos(diameter)) return { error: "the round diameter must be above zero" };
    if (!pos(factor)) return { error: "the wood factor must be above zero" };
    if (!pos(rating)) return { error: "the box tonnage must be above zero" };
    var needed = diameter * factor;
    var margin = rating / needed * 100;
    var verdict = margin >= 100 ? "the ram covers the round"
      : margin >= 80 ? "the ram stalls on the tough ones"
      : "the ram is outclassed";
    return { needed: r1(needed), margin: r1(margin), verdict: verdict };
  }
  function renderTonnage(r, diameter, factor, rating) {
    var word = factor === 1 ? " ton an inch" : " tons an inch";
    return "At " + jsnum(diameter) + " inches and " + jsnum(factor) + word + ", the round wants " + jsnum(r.needed)
      + " honest tons; the " + jsnum(rating) + "-ton box sits at " + jsnum(r.margin) + "% of that, and " + r.verdict + ".";
  }
  function cyclePlan(sticker) {
    if (!pos(sticker)) return { error: "the sticker cycle must be above zero" };
    var honest = sticker * LOAD;
    return { honest: r1(honest), perHour: r1(3600 / honest) };
  }
  function renderCycle(r, sticker) {
    return "The " + jsnum(sticker) + "-second cycle on the sticker is the empty ram; under load the honest cycle is about "
      + jsnum(r.honest) + " seconds, a pace of about " + jsnum(r.perHour) + " rounds an hour.";
  }
  function circuitPlan(amps, claimedHp) {
    if (!pos(amps)) return { error: "the circuit amps must be above zero" };
    if (!pos(claimedHp)) return { error: "the claimed horsepower must be above zero" };
    var honest = VOLTS * amps * EFF / W_PER_HP;
    var ratio = claimedHp / honest;
    var verdict = ratio <= 1 ? "the sticker fits the circuit"
      : ratio <= 2 ? "the sticker counts the startup surge"
      : "the sticker is marketing first";
    return { honest: r2(honest), ratio: r2(ratio), verdict: verdict };
  }
  function renderCircuit(r, amps, claimedHp) {
    return "The " + jsnum(amps) + "-amp circuit honestly feeds about " + jsnum(r.honest)
      + " horsepower after the continuous-load derate; the " + jsnum(claimedHp) + "-horsepower sticker claims "
      + jsnum(r.ratio) + " times that, and " + r.verdict + ".";
  }
  return { tonnagePlan: tonnagePlan, renderTonnage: renderTonnage, cyclePlan: cyclePlan, renderCycle: renderCycle, circuitPlan: circuitPlan, renderCircuit: renderCircuit };
})();
if (typeof module !== "undefined" && module.exports) module.exports = SplitMath;
