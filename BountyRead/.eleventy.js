const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

module.exports = function (eleventyConfig) {
  // Add json filter
  eleventyConfig.addFilter("json", function (value) {
    return JSON.stringify(value);
  });

  // Existing passthrough copy or other configs (if any)
  eleventyConfig.addPassthroughCopy("assets");

  // Optional: Add Markdown filter if not already present (for report.njk)
  const markdownIt = require("markdown-it");
  const markdownLib = markdownIt({ html: true });
  eleventyConfig.addFilter("markdown", function (value) {
    return markdownLib.render(value || "");
  });

  eleventyConfig.addPassthroughCopy({"favicon/": "/"});
  return {
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    templateFormats: ["njk", "html"],
    htmlTemplateEngine: "njk",
  };
};
