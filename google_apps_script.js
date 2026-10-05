/**
 * =========================================================================
 * 🎨 CONCEPT ARTIST JOB TRACKER - GOOGLE APPS SCRIPT AUTOMATION
 * =========================================================================
 * 
 * HOW TO USE (Zero coding required):
 * 1. Open your Google Sheet (create a blank one at https://sheets.new).
 * 2. In the top menu, click: Extensions > Apps Script.
 * 3. Delete any text in the editor, paste this entire file, and click the Save icon (💾).
 * 4. Close the Apps Script tab and refresh your Google Sheet.
 * 5. You will see a new menu in Google Sheets: "🎨 Art Job Tracker".
 * 6. Click "🎨 Art Job Tracker" > "1. Initialize / Reformat Tracker".
 *    (Google will ask for permission once; click Advanced > Proceed).
 * =========================================================================
 */

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🎨 Art Job Tracker')
    .addItem('✨ 1. Initialize / Reformat Tracker', 'initializeJobTracker')
    .addSeparator()
    .addItem('📅 2. Sort by Date Posted (Newest First)', 'sortByDatePosted')
    .addItem('🌐 3. Sort by Source Site', 'sortBySourceSite')
    .addSeparator()
    .addItem('➕ 4. Add Blank Job Row at Top', 'insertNewJobAtTop')
    .addToUi();
}

/**
 * Initializes header styling, column widths, dropdowns, conditional colors, and filters.
 */
function initializeJobTracker() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // 1. Column Headers
  const headers = [
    "Job Title",
    "City / Country",
    "Link to Job Post",
    "Requirements",
    "Remote or Not / Else",
    "Level of Seniority",
    "Status",
    "Date Posted",
    "Source Site"
  ];
  
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  
  // Header Style (Modern Dark Theme)
  const headerRange = sheet.getRange(1, 1, 1, headers.length);
  headerRange
    .setBackground("#1E293B")
    .setFontColor("#FFFFFF")
    .setFontWeight("bold")
    .setFontFamily("Plus Jakarta Sans, Inter, Roboto, Arial")
    .setFontSize(11)
    .setHorizontalAlignment("center")
    .setVerticalAlignment("middle")
    .setWrap(true);
  
  sheet.setRowHeight(1, 40);
  sheet.setFrozenRows(1);

  // 2. Set Optimal Column Widths
  sheet.setColumnWidth(1, 240); // Job Title
  sheet.setColumnWidth(2, 170); // City / Country
  sheet.setColumnWidth(3, 200); // Link to Job Post
  sheet.setColumnWidth(4, 340); // Requirements
  sheet.setColumnWidth(5, 150); // Remote or Not / Else
  sheet.setColumnWidth(6, 140); // Level of Seniority
  sheet.setColumnWidth(7, 210); // Status
  sheet.setColumnWidth(8, 120); // Date Posted
  sheet.setColumnWidth(9, 160); // Source Site

  const maxRows = Math.max(sheet.getMaxRows(), 100);

  // 3. Dropdown for "Remote or Not / Else" (Column E / Col 5)
  const remoteRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(["Remote", "Hybrid", "On-site", "Global Remote (Contract)", "Freelance"], true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 5, maxRows - 1, 1).setDataValidation(remoteRule);

  // 4. Dropdown for "Level of Seniority" (Column F / Col 6)
  const seniorityRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(["Junior / Associate", "Mid-level", "Senior", "Lead / Principal", "Open / Any Level"], true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 6, maxRows - 1, 1).setDataValidation(seniorityRule);

  // 5. Dropdown for "Status" (Column G / Col 7)
  const statusValues = [
    "🟣 Discovered / Bookmarked",
    "🟡 Applied / Waiting",
    "🟠 Recruiter Screen / Contacted",
    "🔵 Art Test / Assignment",
    "🟢 Interviewing (Portfolio / Team)",
    "🏆 Offer Received",
    "🔴 Rejected",
    "⚪ Archived / No Response"
  ];
  
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(statusValues, true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 7, maxRows - 1, 1).setDataValidation(statusRule);

  // 6. Format Date Column (Column H / Col 8)
  sheet.getRange(2, 8, maxRows - 1, 1).setNumberFormat("yyyy-mm-dd");

  // 7. Enable Text Wrapping on Requirements
  sheet.getRange(2, 4, maxRows - 1, 1).setWrap(true);

  // 8. Conditional Formatting for Status Colors
  setupStatusColors(sheet, maxRows);

  // 9. Enable Auto-filter
  if (sheet.getFilter() !== null) {
    sheet.getFilter().remove();
  }
  sheet.getRange(1, 1, maxRows, headers.length).createFilter();

  SpreadsheetApp.getUi().alert("✅ Success! Your Art Job Tracker has been formatted with dropdowns, color-coded statuses, and auto-filters.");
}

/**
 * Builds conditional formatting rules for the Status column
 */
function setupStatusColors(sheet, maxRows) {
  const statusRange = sheet.getRange(2, 7, maxRows - 1, 1);
  const rules = [];

  const colorMap = [
    { text: "🟣 Discovered / Bookmarked", bg: "#F3E8FF", fg: "#6B21A8" },
    { text: "🟡 Applied / Waiting", bg: "#FEF3C7", fg: "#92400E" },
    { text: "🟠 Recruiter Screen / Contacted", bg: "#FFEDD5", fg: "#9A3412" },
    { text: "🔵 Art Test / Assignment", bg: "#DBEAFE", fg: "#1E40AF" },
    { text: "🟢 Interviewing (Portfolio / Team)", bg: "#D1FAE5", fg: "#065F46" },
    { text: "🏆 Offer Received", bg: "#ECFDF5", fg: "#047857" },
    { text: "🔴 Rejected", bg: "#FEE2E2", fg: "#991B1B" },
    { text: "⚪ Archived / No Response", bg: "#F3F4F6", fg: "#4B5563" }
  ];

  for (let i = 0; i < colorMap.length; i++) {
    const item = colorMap[i];
    const rule = SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo(item.text)
      .setBackground(item.bg)
      .setFontColor(item.fg)
      .setBold(true)
      .setRanges([statusRange])
      .build();
    rules.push(rule);
  }

  sheet.setConditionalFormatRules(rules);
}

/**
 * Sorts all active rows by Date Posted (Column H) - Newest to Oldest
 */
function sortByDatePosted() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();
  if (lastRow <= 1) return;

  // Range from row 2 to last row, sorted by col 8 (Date Posted) descending
  const dataRange = sheet.getRange(2, 1, lastRow - 1, lastCol);
  dataRange.sort([
    { column: 8, ascending: false }, // Date posted: newest first
    { column: 9, ascending: true }   // Then by Source site
  ]);
  SpreadsheetApp.getActiveSpreadsheet().toast("Sorted by Date Posted (Newest First)", "Sort Complete", 3);
}

/**
 * Sorts all active rows by Source Site (Column I), then by Date Posted
 */
function sortBySourceSite() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();
  if (lastRow <= 1) return;

  const dataRange = sheet.getRange(2, 1, lastRow - 1, lastCol);
  dataRange.sort([
    { column: 9, ascending: true },  // Source Site A-Z
    { column: 8, ascending: false }  // Then newest date
  ]);
  SpreadsheetApp.getActiveSpreadsheet().toast("Sorted by Source Site", "Sort Complete", 3);
}

/**
 * Inserts a blank row directly below the header for easy manual entry
 */
function insertNewJobAtTop() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.insertRowBefore(2);
  sheet.getRange(2, 7).setValue("🟣 Discovered / Bookmarked");
  sheet.getRange(2, 8).setValue(new Date());
  SpreadsheetApp.getActiveSpreadsheet().toast("New row inserted at row 2 with today's date", "Row Added", 3);
}
