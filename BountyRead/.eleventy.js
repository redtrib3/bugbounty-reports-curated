const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

module.exports = function (eleventyConfig) {
  eleventyConfig.addFilter("json", function (value) {
    return JSON.stringify(value);
  });

  eleventyConfig.addPassthroughCopy("assets");
  
  const markdownIt = require("markdown-it");
  const markdownLib = markdownIt({ html: true });
  eleventyConfig.addFilter("markdown", function (value) {
    return markdownLib.render(value || "");
  });

  eleventyConfig.addPassthroughCopy({"favicon/": "/"});
  eleventyConfig.addPassthroughCopy("robots.txt")
  eleventyConfig.addPassthroughCopy("sitemap.xml")

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
