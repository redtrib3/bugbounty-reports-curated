const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

function escapeJsonString(str) {
  if (!str) return "";
  // neutralize script tags and other HTML that could break the script context
  let sanitized = str
    .replace(/<\/script>/gi, "<\\/script>") // Escape </script> to prevent tag closure
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, "") // Remove <script> blocks
    .replace(/<!--[\s\S]*?-->/g, "") // Remove HTML comments
    .replace(/<\/?[a-z][\s\S]*?>/gi, ""); // Remove all other HTML tags
  sanitized = sanitized
    .replace(/\\/g, "\\\\") // Escape backslashes
    .replace(/\r/g, "\\r")  // Escape carriage returns
    .replace(/\t/g, "\\t"); // Escape tabs
  return sanitized;
}


const dir = "../reports"; 
const files = fs.readdirSync(dir).filter(f => f.endsWith(".yaml") || f.endsWith(".yml"));

const reportsArray = files.map(file => {
  const content = fs.readFileSync(path.join(dir, file), "utf8");
  const data = yaml.load(content);
  const slug = file.replace(/\.ya?ml$/, "");
  const [rawDate, target] = slug.split("-");
  //const dateFormatted = `${rawDate.slice(6, 8)}-${rawDate.slice(4, 6)}-${rawDate.slice(0, 4)}`;
  const dateFormatted = `${rawDate.slice(0, 4)}-${rawDate.slice(4, 6)}-${rawDate.slice(6, 8)}`; // YYYY-MM-DD

  const referencesArray = Array.isArray(data.references) ? data.references : (data.references ? [data.references] : []);
  const tagsArray = Array.isArray(data.tags) ? data.tags : (data.tags ? [data.tags] : []);

  const sanitizedData = {
    ...data,
    summary: escapeJsonString(data.summary || ""),
    references: referencesArray.map(escapeJsonString),
    title: escapeJsonString(data.title || ""),
    bug_type: escapeJsonString(data.bug_type || ""),
    program: escapeJsonString(data.program || data.target || ""),
    tags: tagsArray.map(escapeJsonString),
  };

  return {
    id: slug,
    target: target,
    date: dateFormatted,
    path: `/reports/${slug}/`,
    ...sanitizedData,
  };
});
module.exports = reportsArray;
