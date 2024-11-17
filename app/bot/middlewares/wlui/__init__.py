"""Webhook Logging User ID (WLUI) Module

This module provides a comprehensive logging system for Telegram bots that tracks and manages
contextual information across asynchronous operations. It implements a middleware-based approach
to capture and maintain logging context for various Telegram bot events.

Key Components:
--------------
- WLUIContextVar: A singleton context manager that maintains request-scoped variables
- WnLoggingUserIdMiddleware: Middleware that intercepts Telegram events and manages logging context
- WLUIFilter: A logging filter that enriches log records with contextual information
- Formatter: Custom log formatter that includes WLUI-specific fields

Features:
---------
1. Context Management:
   - Tracks message IDs, bot IDs, chat IDs, and chat types
   - Maintains context across asynchronous operations
   - Thread-safe context variable implementation
   - Singleton pattern for global state management

2. Event Handling:
   - Supports multiple Telegram event types:
     * Regular messages
     * Edited messages
     * Channel posts
     * Edited channel posts
     * Inline queries
     * Chosen inline results

3. Logging Enhancement:
   - Enriches log records with contextual information
   - Custom formatting for improved debugging
   - Consistent logging across the application

Usage Example:
-------------
    from app.bot.middlewares.wlui import WLUIContextVar, WnLoggingUserIdMiddleware

    # Initialize context
    wlui = WLUIContextVar()

    # Setup middleware
    dp.middleware.setup(WnLoggingUserIdMiddleware(wlui))

    # Configure logging
    logger = logging.getLogger(__name__)
    logger.addFilter(WLUIFilter())

Note:
-----
This module is designed to work seamlessly with aiogram-based Telegram bots and
provides essential logging context for debugging and monitoring bot operations.
"""
